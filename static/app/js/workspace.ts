/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />

module Workspace{
    class Workspace {
        constructor() {
            var mainMenu:Menus.MainMenu = new Menus.MainMenu();
            mainMenu.populate(
            [
                {label: 'menu item1'},
                {label: 'hgjgjghjgjgj', icon: 'hello'},
                {label: 'sadadssa'}
            ]
            );
        }
        body: JQuery;
        test() {
            return ("hello");
        }
    }
}