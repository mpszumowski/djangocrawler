$(document).ready(function() {

    $.ajax({
        url: 'http://127.0.0.1:8000/countries/'
    }).done(function(data) {

        var tbody = $("tbody");

        for (var i = 0; i < data.length; i++) {
            var name = data[i].name;
            // limit data to countries and World
            if (name == "East Asia & Pacific") {
                break
            }
            // clean and parse population data
            var population = data[i].population[0].estimate;
            if (population == "0.0") {
                var population = "0.01";
            }
            if (population == "..") {
                var population = "5.0"
            }
            var population = population.replace(",", "")
            // clean poverty data
            if (data[i].poverty.length != 0) {
                var poverty = data[i].poverty[0].percent
            } else {
                var poverty = "brak danych"
            }
            // clean amount data
            if (data[i].amount.length != 0) {
                var amount = data[i].amount[0].amount;
                if (amount == "?") {
                    var amount = "dane niepełne"
                }
            } else {
                var amount = "brak danych"
            }
            var countryInfo = $(`
                <tr data-region="${name}">
                    <td>${name}</td>
                    <td>${population}</td>
                    <td>${poverty}</td>
                    <td>${amount}</td>
                </tr>
            `);
            tbody.append(countryInfo);
        }
            var footer = $("footer");
        footer.append('<button id="fixedButton">Losuj</button>');

        // add event to button
        $("#fixedButton").on('click', function(event) {
            var worldTotal = $('[data-region="World"] > td')[1];
            var regionList = $("td:first-child");
            var populationList = $("td:nth-child(2)");
            var country = getRandomCountry(regionList,
                populationList,
                worldTotal);
            var row = $(country).parent();
            $("tr").removeClass("active");
            $(row).toggleClass("active");
            var offset = $(row).offset();
            console.log(country);
            $('html, body').animate({
                scrollTop: offset.top
            });
        });

        footer.append('<div><button>' +
            '<span id="actualize">Aktualizuj dane</span></button></div>');
        $("#actualize").on('click', function(event) {
            $.ajax({
            url: 'http://127.0.0.1:8000/update/'
            }).done(function(data) {
                $(location).attr('href', 'http://127.0.0.1:6800/jobs');
                // location.reload(true)
            })
        })
    });
    // function drawing from random country in the world
    var random = function(upperLimit) {
        return Math.random() * upperLimit
    };
    // enter lists from name column, pop column and total world population
    var getRandomCountry = function(list, weight, max) {
        var max = parseFloat($(max).text());
        var sample = random(max);
        var total = 0;
        for (var i = 0; i < list.length; i++) {
            var total = parseFloat(weight[i].innerText) + total;
            if (total > sample) {
                return list[i]
            }
        }
        var randomNum = random(total)
    };
});




