$("#search-form").submit(function(event) {
    event.preventDefault();
    var searchQuery = $("#search-input").val();
    $.ajax({
        url: '/results',
        data: {query: searchQuery},
        type: 'POST',
        success: function(response) {
            // Actualizar el contenido de la página con los resultados de búsqueda
            $("#search-results").html(response);
        }
    });
});