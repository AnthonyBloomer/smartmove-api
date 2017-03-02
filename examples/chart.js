/**
 * Created by anthonybloomer on 27/01/2017.
 */

google.load('visualization', '1.0', {'packages': ['corechart', 'table'], 'callback': drawCharts});


function drawPie() {
    var json = $.ajax({
        url: "http://0.0.0.0:33507/charts/counties/average-sale-price",
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

function getTableData() {
    var json = $.ajax({
        url: "http://0.0.0.0:33507/charts/table",
        dataType: "json",
        async: false
    }).responseText;
    console.log(json);
    var data = new google.visualization.DataTable(json);
    var table = new google.visualization.Table(document.getElementById('table'));
    table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
}

function drawCharts() {
    drawPie();
    getTableData();
}

