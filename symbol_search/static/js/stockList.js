$(document).ready(function(){
    let searchForm = $('#stock-search-input')
    searchForm.on('submit', function(){
        $('.loading-container').show()
    })
})