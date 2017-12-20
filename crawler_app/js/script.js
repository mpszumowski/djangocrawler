$(document).ready(function() {


    $.ajax({
        url: 'http://127.0.0.1:8000/countries/'
    }).done(function(data) {
        var main = $("main");

        for (var i = 0; i < data.length; i++) {
            var countryInfo = $(`
                <tr>
                    <td>${data[i].name}</td>
                    <td>${data[i].population[0].estimate}</td>
                    <td>${data[i].poverty[0].percent}</td>
                    <td>${data[i].amount[0]}</td>
                </tr>
            `);
            main.append(countryInfo);
        }
    });
});



