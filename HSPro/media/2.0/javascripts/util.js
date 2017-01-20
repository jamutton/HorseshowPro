function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = Cookies.get('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function render_show_list(element) {
  var mySuccess = function( data ) {
    var templateEntry = $('#showModalSample').clone();
    $('#showModalSample').remove();
    for (var i=0;i<data.length;i++) {
      var show = data[i];
      var p = show.pk;
      var n = show.fields.Name;
      var d = show.fields.Date;
      var $newEntry = templateEntry.clone();
      $newEntry.find('#showModalSampleLink').html('<a href="/HSPro/'+p+'">'+n+' - '+d+'</a>');
      $("<p>").append($newEntry).appendTo('#showModalBody');
      //$newEntry.appendTo('#showModalBody');
    }
  };

  var myError = function(jqXHR, textStatus, errorThrown) {
    $('#showModalBody').html('<p class="errorMessage">Error: ' + errorThrown + '</p>');
  };

  $.ajax({
    dataType: "json",
    url: '/HSPro/shows/json/',
    success: mySuccess,
    error: myError
  });
}

function submitCSV(myData, showid) {
  var mySuccess = function(data) {
    $('#csvModalBody').html('<div class="alert alert-success" role="alert"><strong>' + JSON.stringify(data) + '</strong></div>');
  };
  var myError = function(jqXHR, textStatus, errorThrown) {
    $('#csvModalBody').html('<div class="alert alert-danger" role="alert">Unable to complete import.  The error was: <strong>' + errorThrown + '</strong></div>');
  };

  $.ajax({
    contentType: "text/csv",
    dataType: "json",
    url: '/HSPro/shows/'+ showid + '/entryimport/',
    type: "POST",
    data: myData,
    success: mySuccess,
    error: myError
  });
};

var docHead = document.getElementsByTagName('head')[0];
var newLinkNode = document.createElement('link');
newLinkNode.rel = 'shortcut icon';
newLinkNode.href = 'data:image/png;base64,AAABAAIAEBEAAAEAIACsBAAAJgAAABAQAgABAAEAsAAAANIEAAAoAAAAEAAAACIAAAABACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAAAP8AAAD/AAAA9wAAAPkAAADyAAAA+QAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAPQAAAD/AAAAKAAAADUAAABJAAAAWAAAANkAAADZAAAA/AAAANoAAACBAAAAfgAAAG4AAACLAAAAIQAAAHAAAACvAAAAPgAAAAEAAAACAAAABQAAAAAAAAADAAAAuAAAAGwAAACtAAAAAAAAAAAAAABWAAAACgAAAAMAAAAAAAAADwAAAA0AAAAAAAAAAQAAAAAAAABPAAAAdgAAADoAAAB6AAAAfgAAACcAAAAAAAAAuAAAAFAAAAAAAAAABQAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAWQAAAGsAAAAAAAAAuwAAAFYAAACTAAAAAAAAADUAAABkAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE4AAAA8AAAAAgAAACIAAADUAAAAmgAAAAEAAAAAAAAAzwAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbAAAAxgAAAB8AAAAAAAAAygAAAPIAAADXAAAAwQAAAP4AAACVAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAABAAAAAAAAAFUAAADxAAAA7gAAAP8AAAD9AAAA/QAAAP0AAAD9AAAA1gAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAzwAAAPoAAAD9AAAA/wAAAP4AAAD+AAAA/AAAAO4AAABIAAAAigAAAAcAAAAAAAAAAAAAAAAAAAADAAAAAAAAAHwAAAD/AAAA+gAAAP8AAAD/AAAA/AAAAPoAAADlAAAAYgAAAOIAAAAVAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAGAAAA0QAAAP8AAAD9AAAA/wAAAP8AAAD/AAAA2wAAANoAAACfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAABQAAADpAAAA/wAAAPIAAACCAAAASAAAAP8AAAD+AAAAagAAAAAAAAABAAAAAAAAAAAAAAADAAAAAAAAAFYAAAD/AAAAlwAAAP8AAADxAAAApQAAADAAAADvAAAAogAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAA4gAAAOAAAADkAAAA/wAAAI8AAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAJIAAAD4AAAA/gAAAPoAAABZAAAAAQAAAAYAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAEAAAAxAAAA4AAAALAAAAC7AAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAwAAAG0AAABLAAAACAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA4NsAAPX/AAD/vwAA+v8AAPzfAADsDwAA8A8AAPALAAD4CwAA+AMAAPwnAAD4JwAA+D8AAPh/AAD8fwAA//8AACgAAAAQAAAAIAAAAAEAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA';
docHead.appendChild(newLinkNode);
