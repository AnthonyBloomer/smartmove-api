/**
 * Created by anthonybloomer on 27/01/2017.
 */

google.charts.load('current', {'packages': ['corechart']});

$("#submit").click(function (e) {
    e.preventDefault();
    var t = $('#text').val();
    drawChart(capitalize(t));
});

function capitalize(s) {
    return s && s[0].toUpperCase() + s.slice(1);
}

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

    json = jQuery.parseJSON(json);


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

$(window).resize(function () {
    drawChart();
});

$(window).load(function (){
   drawChart();
   drawPie();
});

