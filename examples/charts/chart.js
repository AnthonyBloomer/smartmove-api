/**
 * Created by anthonybloomer on 27/01/2017.
 */

google.load('visualization', '1.0', {'packages': ['corechart', 'table'], 'callback': drawCharts});

var URL = 'http://0.0.0.0:33507/';

function ajax(url) {
    return $.ajax({
        url: url,
        dataType: "json",
        async: false
    }).responseText;
}

function draw_pie() {
    var p = ajax(URL + 'charts/counties/average-sale-price');
    var data = new google.visualization.DataTable(p);

    var options = {
        title: 'Top 10 counties by average sale price.'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}

function get_county_price(county) {
    var json = ajax(URL + 'charts/' + county);
    var data = new google.visualization.DataTable(json);
    var options = {
        title: 'Average Sale Price in ' + county,
        hAxis: {title: 'Year'},
        vAxis: {title: 'Average Sale Price'},
        legend: 'none'
    };

    var chart = new google.visualization.LineChart(document.getElementById('county'));
    chart.draw(data, options);
}

function new_dwelling_sales() {
    var dwelling_sales = ajax(URL + 'charts/new-dwellings/number-of-sales');
    var data = new google.visualization.DataTable(dwelling_sales);
    var options = {
        hAxis: {
            title: 'Count'
        },
        vAxis: {
            title: 'Year'
        },
        title: 'Number of sales of new dwellings.'
    };

    var chart = new google.visualization.LineChart(document.getElementById('dwelling_sales'));
    chart.draw(data, options);
}

function new_dwelling_prices() {
    var dwelling_sales = ajax(URL + 'charts/new-dwellings/average-sale-price');
    var data = new google.visualization.DataTable(dwelling_sales);
    console.log(data);
    var options = {
        hAxis: {
            title: 'Price'
        },
        vAxis: {
            title: 'Year'
        },
        title: 'Average sale price of new dwellings.'
    };

    var chart = new google.visualization.LineChart(document.getElementById('dwelling_avgs'));
    chart.draw(data, options);
}

function get_table_data() {
    var t = ajax(URL + 'charts/table');
    var data = new google.visualization.DataTable(t);
    var table = new google.visualization.Table(document.getElementById('table'));
    table.draw(data, {
        showRowNumber: true,
        width: '100%',
        height: '100%',
        title: 'Number of sales and average sale price for each town.'
    });
}

function drawCharts() {
    draw_pie();
    get_county_price('dublin');
    get_table_data();
    new_dwelling_sales();
    new_dwelling_prices();
}


$("#county-avg").click(function () {
    get_county_price($("#option").val());
});