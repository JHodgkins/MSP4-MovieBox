// Update quantity on basket page
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item from basket and reload page
    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var item = $(this).data('remove');
        var url = `/basket/remove/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken, 'remove': item};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })