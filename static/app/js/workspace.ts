/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
/// <reference path="server.ts" />

module Workspace{
    class Workspace {
        constructor() {
            this.body = $('body');

            var mainMenu: Menus.BarMenu = new Menus.BarMenu($('#mainMenu'));
            mainMenu.populate(
                [
                    {label: 'menu item1', 'action': ''},
                    {label: 'hgjgjghjgjgj', 'action': '', icon: 'hello'},
                    {label: 'sadadssa', 'action': ''}
                ]
            );
            this.server = new Server.Server("localhost", "html");
            this.server.get("1", "list", null, 
                function(data){
                    alert(data);
                }
            );

            alert('done init');
        }
        body: JQuery;
        server: Server.Server;
        test() {
            return ('hello from test');
        }
    }

    $(document).ready(
        function(){
            var workspace: Workspace = new Workspace();        
        }
    );
}