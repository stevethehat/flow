/// <reference path="jquery.d.ts" />
/// <reference path="actions.ts" />

module Flow.Menus{
    export interface MenuElement extends Actions.ActionElement{ 
        subElements?:Actions.ActionElements;
    }
    
    export class BarMenu{
        private _container: JQuery;
        private _containerFluid: JQuery;
        private _workspace: Flow.Workspace;
        constructor(workspace: Flow.Workspace, container: JQuery) {
            this._workspace = workspace;
            this._container = container;
            this._container
                .attr('role', 'navigation')
                .addClass('navbar navbar-default');

            this._containerFluid = this._container.append('div')
                .addClass('container-fluid');

            this._containerFluid.append("button")
                .attr('type', 'button');

        }

        populate(elements: Actions.ActionElements): void{
			alert('populate' + elements);
        }

        private addElement(): void {

        }
    }
}