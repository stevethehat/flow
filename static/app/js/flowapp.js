/// <reference path="jquery.d.ts" />
/// <reference path="actions.ts" />
var Menus;
(function (Menus) {
    var BarMenu = (function () {
        function BarMenu(container) {
            this._container = container;
            this._container.attr('role', 'navigation').addClass('navbar navbar-default');

            this._container.append;
        }
        BarMenu.prototype.populate = function (elements) {
            alert("hello");
        };

        BarMenu.prototype.addElement = function () {
        };
        return BarMenu;
    })();
    Menus.BarMenu = BarMenu;
})(Menus || (Menus = {}));
/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
var Workspace;
(function (_Workspace) {
    var Workspace = (function () {
        function Workspace() {
            this.body = $('body');

            var mainMenu = new Menus.BarMenu($('#mainMenu'));
            mainMenu.populate([
                { label: 'menu item1' },
                { label: 'hgjgjghjgjgj', icon: 'hello' },
                { label: 'sadadssa' }
            ]);
            alert('done init');
        }
        Workspace.prototype.test = function () {
            return ('hello from test');
        };
        return Workspace;
    })();
    $(document).ready(function () {
        var workspace = new Workspace();
    });
})(Workspace || (Workspace = {}));
