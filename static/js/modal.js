// sending event ot button for modals 

$(document).on("click", ".delete_javascript", function () {
    var bookingID = $(this).data('id');
    document.getElementById("delete_book").setAttribute("href", "/events/delete_booking/" + bookingID + "/");
});

$(document).on("click", ".cancel-event", function () {
    var eventID = $(this).data('id');
    document.getElementById("cancel_event").setAttribute("href", "/events/cancel_event/" + eventID + "/");
});