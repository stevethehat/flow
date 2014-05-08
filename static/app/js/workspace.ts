/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
/// <reference path="server.ts" />

module Workspace{
    class Workspace {
        constructor() {
            this.body = $('body');

            var mainMenu: Menus.BarMenu = new Menus.BarMenu($('#mainMenu'));

            this.server = new Server.Server("localhost", "html");
            this.server.get("1", "workspacemenu", null, 
                function(data){
                    mainMenu.populate(<Actions.ActionElements>data);
                }
            );
        }
        body: JQuery;
        server: Server.Server;
    }

    $(document).ready(
        function(){
            var workspace: Workspace = new Workspace();        
        }
    );
}