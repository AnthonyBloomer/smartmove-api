/**
 * Created by anthonybloomer on 27/01/2017.
 */

google.load('visualization', '1.0', {'packages': ['corechart'], 'callback': drawCharts});

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

function drawChart(q) {
    q = q || "Dublin";
    $(".title").html(q);
    var json = $.ajax({
        url: "http://127.0.0.1:5000/gcharts/dublin",
        dataType: "json",
        async: false
    }).responseText;

    var data = new google.visualization.DataTable(json);
    var options = {
        title: q + ' Average Sale Price',
        hAxis: {title: 'Year'},
        vAxis: {title: 'Average Sale Price'},
        legend: 'none'
    };

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}

function getTableData(){
    
}

function drawCharts() {
    drawChart();
    drawPie();
}

