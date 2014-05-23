module Flow.Actions {
    'use strict';

    export interface IActionClick {
        (event: any): boolean;
    }

    export interface IActionElement {
        uid: string;
        label: string;
        action: string;
        icon?: string;
    }

    export interface IActionElements {
        [index: number]: IActionElement;
    }
}
