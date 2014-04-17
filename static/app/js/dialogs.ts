module Dialogs{
	export interface Button{
		label: string;
	}
	export interface Buttons{
		[index: number]: Button;
	}
}