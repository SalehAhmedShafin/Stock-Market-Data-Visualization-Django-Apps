document.addEventListener('DOMContentLoaded', function() {
    var ctxLine = document.getElementById('okCanvas2').getContext('2d');
    var ctxBar = document.getElementById('okCanvas3').getContext('2d');
    var ctxMultiAxis = document.getElementById('okCanvas4').getContext('2d');
    var chartLine, chartBar, chartMultiAxis;

    function updateCharts(tradeCode) {
        fetch(`/api/data/?trade_code=${tradeCode}`)
            .then(response => response.json())
            .then(data => {
                if (chartLine) {
                    chartLine.destroy();
                }
                if (chartBar) {
                    chartBar.destroy();
                }
                if (chartMultiAxis) {
                    chartMultiAxis.destroy();
                }

                chartLine = new Chart(ctxLine, {
                    type: 'line',
                    data: {
                        labels: data.dates,
                        datasets: [{
                            label: 'Close Price',
                            data: data.close_prices,
                            borderColor: 'blue',
                            borderWidth: 1,
                            fill: false
                        }]
                    },
                    options: {
                        scales: {
                            x: {
                                type: 'time',
                                time: {
                                    unit: 'day'
                                }
                            },
                            y: {
                                beginAtZero: false
                            }
                        }
                    }
                });

                chartBar = new Chart(ctxBar, {
                    type: 'bar',
                    data: {
                        labels: data.dates,
                        datasets: [{
                            label: 'Volume',
                            data: data.volumes,
                            backgroundColor: 'green',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            x: {
                                type: 'time',
                                time: {
                                    unit: 'day'
                                }
                            },
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });

                chartMultiAxis = new Chart(ctxMultiAxis, {
                    type: 'bar',
                    data: {
                        labels: data.dates,
                        datasets: [
                            {
                                label: 'Close Price',
                                type: 'line',
                                data: data.close_prices,
                                borderColor: 'blue',
                                borderWidth: 1,
                                fill: false,
                                yAxisID: 'line-axis'
                            },
                            {
                                label: 'Volume',
                                type: 'bar',
                                data: data.volumes,
                                backgroundColor: 'green',
                                borderWidth: 1,
                                yAxisID: 'bar-axis'
                            }
                        ]
                    },
                    options: {
                        scales: {
                            x: {
                                type: 'time',
                                time: {
                                    unit: 'day'
                                }
                            },
                            y: [
                                {
                                    id: 'line-axis',
                                    type: 'linear',
                                    position: 'left',
                                    beginAtZero: false
                                },
                                {
                                    id: 'bar-axis',
                                    type: 'linear',
                                    position: 'right',
                                    beginAtZero: true
                                }
                            ]
                        }
                    }
                });
            });
    }

    var dropdown = document.getElementById('tradeCodeDropdown');
    dropdown.addEventListener('change', function() {
        var selectedTradeCode = dropdown.value;
        updateCharts(selectedTradeCode);
    });

    var initialTradeCode = document.getElementById('tradeCodeDropdown').value;
    updateCharts(initialTradeCode);
});