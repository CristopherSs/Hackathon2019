import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Damaged} from '../damaged';
import {HackatonService} from '../hackaton.service';
import {Location} from '@angular/common';


@Component({
    selector: 'app-start',
    templateUrl: './start.page.html',
    styleUrls: ['./start.page.scss'],
})
export class StartPage implements OnInit {
    damaged: Damaged;

    constructor(
        private route: ActivatedRoute,
        private hackathonService: HackatonService,
        private location: Location
    ) {
    }

    ngOnInit() {
        this.getDamaged();
    }

    getDamaged(): void {
        const email_id = this.route.snapshot.paramMap.get('email_id');
        console.log('startpage:' + email_id);
        this.hackathonService.getItem(email_id)
            .subscribe(item => this.damaged = item);
                // this.meeting.push(meeting as unknown as Meeting)
        const aux = this.hackathonService.getItem(email_id);
        console.log((aux));
    }

    goBack(): void {
        this.location.back();
    }

}
