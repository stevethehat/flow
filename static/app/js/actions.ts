module Actions {
    export interface ActionClick {
        (event: any): boolean;
    }

    export interface ActionElement {
        uid: string;
        label: string;
        action: string;
        icon?: string;
    }

    export interface ActionElements {
        [index: number]: ActionElement;
    }
}