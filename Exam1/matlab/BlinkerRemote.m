classdef BlinkerRemote < hgsetget
    properties
        serialBlinker
        
    end

    methods
        function obj = BlinkerRemote()
            URL = ("http://roemigkc-pi400.rose-hulman.edu:8080");
    
            obj.serialBlinker = URL;
            %response = webread(obj.serialBlinker + num2str(port) + "/api/")
        end
        function response = LEDOn(obj)
            response = webread(obj.serialBlinker + "/api/led/on");
             fprintf('%s\n', response);
        end
        function response = LEDOff(obj)
            response = webread(obj.serialBlinker  + "/api/led/off");
             fprintf('%s\n', response);
        end
        function response = Flash(obj, flashes, periodMS)
            response = webread(obj.serialBlinker + "/api/flash/" + num2str(flashes) + "/" + num2str(periodMS));
             fprintf('%s\n', response);
        end
    end
end