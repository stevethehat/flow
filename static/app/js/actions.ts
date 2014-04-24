module Actions {
    export interface ActionClick {
        (event: any): boolean;
    }

    export interface ActionElement {
        label: string;
        icon?: string;
    }

    export interface ActionElements {
        [index: number]: ActionElement;
    }
}