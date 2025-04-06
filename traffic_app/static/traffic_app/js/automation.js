$(document).ready(function() {
    // let currentState = "{{ config.current_state }}";
    // let timer;
    let currentState = initialState;
    let timer;
    // Initialize with values from HTML data attributes
    const stateDurations = {
        'Red': parseInt($('#state-data').data('red')),
        'Yellow': parseInt($('#state-data').data('yellow')),
        'Green': parseInt($('#state-data').data('green'))
    };

    // Initialize traffic light display
    updateTrafficLight();

    // Start automation
    startAutomation();

    // Handle form submission with AJAX
    $('#configForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '',
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            data: $(this).serialize(),
            // success: function(response) {
            //     // Update displayed values
            //     $('.red-duration').text(response.config.red_duration);
            //     $('.yellow-duration').text(response.config.yellow_duration);
            //     $('.green-duration').text(response.config.green_duration);
            //     $('.last-updated').text(response.config.last_updated);
                
            //     // Update local durations
            //     stateDurations.Red = response.config.red_duration;
            //     stateDurations.Yellow = response.config.yellow_duration;
            //     stateDurations.Green = response.config.green_duration;
                
            //     // Restart automation with new values
            //     clearTimeout(timer);
            //     currentState = response.config.current_state;
            //     updateTrafficLight();
            //     startAutomation();
            // }
            success: function(response) {
                // Update displayed values (remove .config from response)
                $('.red-duration').text(response.red_duration);
                $('.yellow-duration').text(response.yellow_duration);
                $('.green-duration').text(response.green_duration);
                $('.last-updated').text(response.last_updated);
                
                // Update local durations
                stateDurations.Red = response.red_duration;
                stateDurations.Yellow = response.yellow_duration;
                stateDurations.Green = response.green_duration;
                
                // Restart automation with new values
                clearTimeout(timer);
                currentState = response.current_state;
                updateTrafficLight();
                startAutomation();
            }
        });
    });

    function startAutomation() {
        let duration = stateDurations[currentState] * 1000;
        let countdown = stateDurations[currentState];
        
        $('.countdown').text(countdown);
        
        timer = setInterval(() => {
            countdown--;
            $('.countdown').text(countdown);
            
            if(countdown <= 0) {
                clearInterval(timer);
                transitionToNextState();
            }
        }, 1000);
    }

    function transitionToNextState() {
        $.post('/update-state/', function(data) {
            currentState = data.current_state;
            $('.current-state-display').text(currentState);
            $('.last-updated').text(data.last_updated);
            updateTrafficLight();
            startAutomation();
        });
    }

    function updateTrafficLight() {
        $('.light').removeClass('active');
        $(`.light.${currentState.toLowerCase()}`).addClass('active');
    }
});