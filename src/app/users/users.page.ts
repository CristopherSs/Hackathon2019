import {Component, OnInit} from '@angular/core';
import {Damaged} from '../damaged';
import {HackatonService} from '../hackaton.service';
import {Router} from '@angular/router';


@Component({
    selector: 'app-users',
    templateUrl: './users.page.html',
    styleUrls: ['./users.page.scss'],
})
export class UsersPage implements OnInit {
    damaged: Damaged[] = [];

    constructor(
        private hackatonService: HackatonService,
        private router: Router,
    ) {
    }

    ngOnInit() {
    }

    add(email: string, name: string, last_name: string, password: string, gender: string, disability: string): void {
        this.hackatonService.postItem({email: email, name, last_name, password, gender, disability} as Damaged)
            .subscribe(damaged => {
                this.damaged.push(damaged as unknown as Damaged);
            });
        this.goStartPage(email);
    }

    goStartPage(email_id: string): void {
        this.router.navigateByUrl('start/' + email_id);
    }
}
