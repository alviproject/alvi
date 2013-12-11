window.actions = {};

$(function () {
    connection = null;
    action_in_progress = false;

    function connect() {
        disconnect();

        connection = new SockJS('http://' + window.location.host + '/rt');
        console.log('Connecting...');

        connection.onopen = function () {
            console.log('Connected.');
            connection.message('init');
            update_ui();
        };

        connection.message = function (message) {
            var scene_id = $("#scene_id").text();
            if (scene_id) {
                var data = {'scene_id': scene_id, 'message': message};
                var message = JSON.stringify(data);
                connection.send(message);
            }
        };

        connection.onmessage = function (e) {
            function run_action(action) {
                //console.log(action);
                var action_type = action[0];
                action_in_progress = true;
                //console.log(action);
                actions[action_type](action[1]);
                action_in_progress = false;
                //console.log("action finished");
            }

            var data = JSON.parse(e.data);
            //console.log(data);

            if( Object.prototype.toString.call(data) === '[object Array]' ) {
                for (var i = 0; i < data.length; ++i) {
                    run_action(data[i]);
                }
            }
            else {
                run_action(data);
            }
            update_data();
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
    name = name.replace("_", " ");
    if(stat.length == 0) {
        $("#stats").append('<li id="'+id+'"><span>'+name+':</span> <span class="value"></span></li>');
        stat = $("#stats").find("#"+id);
    }
    stat.find(".value").text(value);
}

function finish() {
    if(action_in_progress) {
        //TODO
        //setting delay to such high value (1000ms) is an ugly workaround
        //the problem is to make sure that scene rendering was finished before reporting that scene is finished
        //it would be much better to base on events than delay
        setTimeout(finish, 1000);
        return;
    }
    var state = $("#state");
    state.attr("style", "color:red");
    state.text("finished");
}

register_action("update_stats", update_stats);
register_action("finish", finish);