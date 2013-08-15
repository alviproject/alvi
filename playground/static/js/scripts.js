window.actions = {};

$(function () {
    var connection = null;

    function connect() {
        disconnect();

        connection = new SockJS('http://' + window.location.host + '/rt');
        console.log('Connecting...');

        connection.onopen = function () {
            console.log('Connected.');
            var session_id = $("#session_id").text();
            if (session_id) {
                var data = {'session_id': session_id};
                var message = JSON.stringify(data);
                connection.send(message);
            }
            update_ui();
        };

        connection.onmessage = function (e) {
            console.log('Received: ' + e.data);
            var action = JSON.parse(e.data);
            var action_type = action['type'];
            actions[action_type](action);
        };

        connection.onclose = function () {
            console.log('Disconnected.');
            connection = null;
            update_ui();
        };
    }

    function disconnect() {
        if (connection != null) {
            console.log('Disconnecting...');

            connection.close();
            connection = null;
            update_ui();
        }
    }

    function update_ui() {
        //TODO place status somewhere on the page
        if (connection == null || connection.readyState != SockJS.OPEN) {
            $('#status').text('disconnected');
            $('#connect').text('Connect');
        } else {
            $('#status').text('connected (' + connection.protocol + ')');
            $('#connect').text('Disconnect');
        }
    }

    connect();
    update_ui();
});

function max(x, y) {
    return x > y ? x : y;
}

function register_action(name, action) {
    window.actions[name] = action;
}

function update_stats(action) {
    var name = action.name;
    var value = action.value;
    var id = "stats_" + name;
    var stat = $("#stats").find("#"+id);
    if(stat.length == 0) {
        stat = $("#stats").append('<li id="'+id+'"><span>'+name+':</span> <span class="value"></span></li>');
    }
    stat.find(".value").text(value);
}

register_action("update_stats", update_stats)

