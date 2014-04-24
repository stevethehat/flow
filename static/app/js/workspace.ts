/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />

module Workspace{
    class Workspace {
        constructor() {
            this.body = $('body');

            var mainMenu: Menus.BarMenu = new Menus.BarMenu($('#mainMenu'));
            mainMenu.populate(
                [
                    {label: 'menu item1'},
                    {label: 'hgjgjghjgjgj', icon: 'hello'},
                    {label: 'sadadssa'}
                ]
            );
            alert('done init');
        }
        body: JQuery;
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