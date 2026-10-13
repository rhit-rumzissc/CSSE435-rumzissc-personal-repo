classdef BlinkerRemote < hgsetget
    properties
        serialBlinker
        
    end

    methods
        function obj = BlinkerRemote()
            URL = ("http://192.168.1.14:8080");
    
            obj.serialBlinker = URL;
            %response = webread(obj.serialBlinker + num2str(port) + "/api/")
        end
        function response = LEDOn(obj)
            response = webread(obj.serialBlinker + "/api/LED%20ON");
             fprintf('%s\n', response);
        end
        function response = LEDOff(obj)
            response = webread(obj.serialBlinker  + "/api/LED%20OFF");
             fprintf('%s\n', response);
        end
        function response = Flash(obj, flashes, periodMS)
            response = webread(obj.serialBlinker + "/api/" + num2str(flashes) + "/" + num2str(periodMS));
             fprintf('%s\n', response);
        end
    end
end