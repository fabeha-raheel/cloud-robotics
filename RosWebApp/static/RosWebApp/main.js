//Tomtom Maps API
        
const CENTER_LOCATION = {lng: 67.1347, lat: 24.7938};

var map = tt.map({
    key: "xFCS6rzf4y6lvM4OgY2bn2ynXEAZfdaS",
    container: "map",
    center: CENTER_LOCATION,
    zoom: 20,
})

// Websocket Connection
let url = `ws://${window.location.host}/ws/tb3/`
const commSocket = new WebSocket(url);

commSocket.onopen = function(e){
    console.log("Websocket Opened")
    document.getElementById('connection-status').textContent = 'Connected';
}

commSocket.onmessage = function(e){
    let data = JSON.parse(e.data);
    // console.log('Data:', data)

    switch (data.type) {
        case "odom_data":
            document.getElementById('odom_linear_x').textContent = data.odom_linear_x;
            document.getElementById('odom_linear_y').textContent = data.odom_linear_y;
            document.getElementById('odom_linear_z').textContent = data.odom_linear_z;

            document.getElementById('odom_angular_x').textContent = data.odom_angular_x;
            document.getElementById('odom_angular_y').textContent = data.odom_angular_y;
            document.getElementById('odom_angular_z').textContent = data.odom_angular_z;

        case "imu_data":
            document.getElementById('imu_orient_x').textContent = data.imu_orient_x;
            document.getElementById('imu_orient_y').textContent = data.imu_orient_y;
            document.getElementById('imu_orient_z').textContent = data.imu_orient_z;
            document.getElementById('imu_orient_w').textContent = data.imu_orient_w;

            document.getElementById('imu_angVel_x').textContent = data.imu_angVel_x;
            document.getElementById('imu_angVel_y').textContent = data.imu_angVel_y;
            document.getElementById('imu_angVel_z').textContent = data.imu_angVel_z;

            document.getElementById('imu_linearAcc_x').textContent = data.imu_linearAcc_x;
            document.getElementById('imu_linearAcc_y').textContent = data.imu_linearAcc_y;
            document.getElementById('imu_linearAcc_z').textContent = data.imu_linearAcc_z;

        case "video_data":

            const frameImageElement = document.getElementById('frameImage');
                        frameImageElement.src = "data:image/jpeg;base64," + data.frame; // Assuming the frame is in JPEG format
        
        case "cmd_vel":

        default:
            // console.log("Received: ", e)
            // throw new Error(`Unsupported event type: ${e.type}.`);
            
        }
    }

commSocket.onerror = function(e){
    console.log('Websocket error: ', e);
}

const upButton = document.getElementById('upBtn');
upButton.addEventListener("click", () => {
    console.log("Up Button clicked")
    message = {
        'type': "cmd_vel",
        'data': {
            linear_x: 0.2,
            linear_y: 0,
            linear_z: 0,
            angular_x: 0,
            angular_y: 0,
            angular_z: 0,
        }
    }
    commSocket.send(JSON.stringify(message))
    console.log(message)
    console.log("JSON Message sent")
});

const downButton = document.getElementById('downBtn');
downButton.addEventListener("click", () => {
    console.log("Down Button clicked")
    message = {
        'type': "cmd_vel",
        'data': {
            linear_x: -0.2,
            linear_y: 0,
            linear_z: 0,
            angular_x: 0,
            angular_y: 0,
            angular_z: 0,
        }
    }
    commSocket.send(JSON.stringify(message))
    console.log(message)
    console.log("JSON Message sent")
});

const leftButton = document.getElementById('leftBtn');
leftButton.addEventListener("click", () => {
    console.log("Left Button clicked")
    message = {
        'type': "cmd_vel",
        'data': {
            linear_x: 0,
            linear_y: 0,
            linear_z: 0,
            angular_x: 0,
            angular_y: 0,
            angular_z: 0.2,
        }
    }
    commSocket.send(JSON.stringify(message))
    console.log(message)
    console.log("JSON Message sent")
});

const rightButton = document.getElementById('rightBtn');
rightButton.addEventListener("click", () => {
    console.log("Right Button clicked")
    message = {
        'type': "cmd_vel",
        'data': {
            linear_x: 0,
            linear_y: 0,
            linear_z: 0,
            angular_x: 0,
            angular_y: 0,
            angular_z: -0.2,
        }
    }
    commSocket.send(JSON.stringify(message))
    console.log(message)
    console.log("JSON Message sent")
});

const stopButton = document.getElementById('stopBtn');
stopButton.addEventListener("click", () => {
    console.log("Stop Button clicked")
    message = {
        'type': "cmd_vel",
        'data': {
            linear_x: 0,
            linear_y: 0,
            linear_z: 0,
            angular_x: 0,
            angular_y: 0,
            angular_z: 0,
        }
    }
    commSocket.send(JSON.stringify(message))
    console.log(message)
    console.log("JSON Message sent")
});