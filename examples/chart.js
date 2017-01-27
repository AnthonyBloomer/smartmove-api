/**
 * Created by anthonybloomer on 27/01/2017.
 */

google.load('visualization', '1.0', {'packages': ['corechart', 'table'], 'callback': drawCharts});

function drawPie() {
    var json = $.ajax({
        url: "http://127.0.0.1:5000/gcharts/pie",
        dataType: "json",
        async: false
    }).responseText;

    var data = new google.visualization.DataTable(json);

    var options = {
        title: 'Average sale price'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}

function drawChart() {
    var json = $.ajax({
        url: "http://127.0.0.1:5000/gcharts/dublin",
        dataType: "json",
        async: false
    }).responseText;

    var data = new google.visualization.DataTable(json);
    var options = {
        title: 'Average Sale Price',
        hAxis: {title: 'Year'},
        vAxis: {title: 'Average Sale Price'},
        legend: 'none'
    };

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}

function getTableData() {
    var json = $.ajax({
        url: "http://127.0.0.1:5000/gcharts/table",
        dataType: "json",
        async: false
    }).responseText;
    console.log(json);
    var data = new google.visualization.DataTable(json);
    var table = new google.visualization.Table(document.getElementById('table'));
    table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
}

function drawCharts() {
    drawChart();
    drawPie();
    getTableData();
}

