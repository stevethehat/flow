/// <reference path="jquery.d.ts" />
/// <reference path="actions.ts" />

module Menus{
    export interface MenuElement extends Actions.ActionElement{ 
        subElements?:Actions.ActionElements;
    }
    
    export class BarMenu{
        private _container: JQuery;
        constructor(container: JQuery) {
            this._container = container;
            this._container
                .attr('role', 'navigation')
                .addClass('navbar navbar-default');

            this._container.append
        }

        populate(elements: Actions.ActionElements): void{
			alert("hello");
        }

        private addElement(): void {

        }
    }
}