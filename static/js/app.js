$('body').on('click', '.rate', function(event){
    let description = $("#description").val();
    // alert(description);
    //trigger function to remove from database
    const url = "/send"

    fetch(url, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(description)
    })
    .then(window.location("/"));
    //event.preventDefault();
    // desc = {"description":description}
    //   $.ajax({
    //     type:'POST',
    //     url:url,
    //     data: {description: description},
    //     contentType: 'application/json; charset=utf-8',
    //     dataType: 'json'
    //     // success:function(response)
    //     // {
    //     //   window.location("/");
    //     // }
    //   });
    
});
