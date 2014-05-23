/// <reference path="libdef/jquery.d.ts" />
/// <reference path="actions.ts" />

module Flow.Menus {
    'use strict';

    export interface IMenuElement extends Actions.IActionElement {
        subElements?: Actions.IActionElements;
    }
    
    export class BarMenu {
        private _container: JQuery;
        private _containerFluid: JQuery;
        private _workspace: Workspace;
        constructor(workspace: Workspace, container: JQuery) {
            this._workspace = workspace;
            this._container = container;
            this._container
                .attr('role', 'navigation')
                .addClass('navbar navbar-default');

            this._containerFluid = this._container.append('div')
                .addClass('container-fluid');

            this._containerFluid.append('button')
                .attr('type', 'button');

        }

        populate(elements: Actions.IActionElements): void{
			alert('populate' + elements);
        }
    }
}
