$(document).ready(function() {
    // add loader during ajax request
    var $body = $("body");
    $body.addClass("loading");
    $.ajax({
        url: 'http://127.0.0.1:8000/countries/'
    }).done(function(data) {
        $body.removeClass("loading");
        var tbody = $("tbody");
        // create table
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

        // add draw, scroll and highlight event to button
        $("#fixedButton").on('click', function(event) {
            // draw country
            var worldTotal = $('[data-region="World"] > td')[1];
            var regionList = $("td:first-child");
            var populationList = $("td:nth-child(2)");
            var country = getRandomCountry(regionList,
                populationList,
                worldTotal);
            var row = $(country).parent();
            // highlight red if under poverty rate, blue if above
            // and yellow if data lacking
            $("tr").removeClass("bg-danger bg-primary bg-warning");
            var minimum = $(row).children()[3].innerText;
            var poverty = $(row).children()[2].innerText;
            if (isNaN(parseFloat(minimum)) || poverty == "..") {
                $(row).toggleClass("bg-warning")
            } else {
                var amount = parseFloat(minimum);
                // add arbitrary modificator in case of populations where
                // minimum is below the poverty rate of $3.10
                if (amount > 3.10) {
                    var mod = 1;
                    if (enoughFood(poverty, mod) == true) {
                        $(row).toggleClass("bg-primary");
                    } else {
                        $(row).toggleClass("bg-danger");
                    }
                } else {
                    var mod = 0.5;
                    if (enoughFood(poverty, mod) == true) {
                        $(row).toggleClass("bg-primary");
                    } else {
                        $(row).toggleClass("bg-danger");
                    }
                }
            }
            // add scroll event
            var offset = $(row).offset();
            $('html, body').animate({
                scrollTop: offset.top
            });
        });
        // actualize function
        footer.append('<div><button class="refresh">' +
            '<span id="actualize">Aktualizuj dane</span></button></div>');
        $("#actualize").on('click', function(event) {
            $.ajax({
                url: 'http://127.0.0.1:8000/update/',
                type: 'POST'
            // launch scrapers with POST method
            // add loading animation and access view with GET method
            // each 2 seconds
            // if each task status == "finished" reload page
            // else repeat GET
            }).done(function(scrapersData) {
                $body.addClass("loading");
                pageReload();
                function pageReload() {
                    $.ajax({
                        url: 'http://127.0.0.1:8000/update/',
                        type: 'GET',
                        data: scrapersData
                    }).done(function(data) {

                        function checkStatus() {
                            for (var p in data) {
                                if (data.hasOwnProperty(p)) {
                                    if (data[p] == "finished") {
                                    } else {
                                        return false
                                    }
                                }
                            }
                            return true
                        }
                        if (checkStatus() == true) {
                            location.reload(true)
                        } else {
                            setTimeout(pageReload, 2000)
                        }
                    })
                }
            })
        })
    });


    // function drawing from random country in the world
    var random = function(upperLimit) {
        return Math.random() * upperLimit
    };
    // enter lists from name column, population column
    // and total world population
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
    };
    // check if enough food
    var enoughFood = function(percent, modificator) {
        if ((Math.random() * 100) > (parseFloat(percent) * modificator)){
            return true
        } else {
            return false
        }
    }
});





            //     // $(location).attr('href', 'http://127.0.0.1:6800/jobs');
            //     // location.reload(true)
