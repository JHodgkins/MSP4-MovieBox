// Update quantity on basket page
    $('.update-link').click(function(e) {
        let form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item from basket and reload page
    $('.remove-item').click(function(e) {
        let csrfToken = "{{ csrf_token }}";
        let itemId = $(this).attr('id').split('remove_')[1];
        let item = $(this).data('remove');
        let url = `/basket/remove/${itemId}/`;
        let data = {'csrfmiddlewaretoken': csrfToken, 'remove': item};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })