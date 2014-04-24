/// <reference path="jquery.d.ts" />

module Menus{
				export interface MenuClick{
								(event: any): boolean;
				}

				export interface MenuElement{
								label: string;
								icon?: string;
				}

				export interface MenuElements{
								[index: number]: MenuElement;
				}

				export class MainMenu{
								populate(elements: MenuElements){
												return("hello");
								}
				}
}