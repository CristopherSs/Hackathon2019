import {Component, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {Damaged} from '../damaged';
import {HackatonService} from '../hackaton.service';

@Component({
    selector: 'app-home',
    templateUrl: 'home.page.html',
    styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {
    damaged: Damaged [] = [];

    constructor(private router: Router,
                private hackathonService: HackatonService) {
    }

    ngOnInit() {
    }

    goRegisterPerson(): void {
        this.router.navigateByUrl('users');
    }

    signIn(email: string, password: string): void {
        this.hackathonService.getItemTest(email, password);
        console.log(email, password);
    }

}
