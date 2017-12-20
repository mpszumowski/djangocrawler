$(document).ready(function() {


    $.ajax({
        url: 'http://127.0.0.1:8000/countries/'
    }).done(function(data) {
        var main = $("main");

        for (let i = 0; i < data.length; i++) {

            let bookInfo = $(`
                <button type="button" data-id="${data[i].id}" 
                class="list-group-item list-group-item-action">${data[i].title}
                    <div style="display:none">
                        <ul style="list-style-type: none;">
                            <li>Autor: ${data[i].author}</li>
                            <li>Gatunek: ${data[i].genre}</li>
                            <li>Wydawnictwo: ${data[i].publisher}</li>
                            <li>ISBN: ${data[i].isbn}</li>
                            <li>ID: ${data[i].id}</li>
                        </ul>
                    </div>
                </button>
            `);
            main.append(bookInfo);
        }
        $("button").on('click', function() {
            const allButtons = $("button");
            allButtons.removeClass("active");
            $(this).toggleClass("active");
            let childDiv = $(this).find("div");
            allButtons.find("div").css("display", "none")
            $(childDiv).fadeIn(500);

        });

    });
});



