import { Component, OnInit } from '@angular/core';
import { Damaged } from '../damaged';
import { HackatonService } from '../hackaton.service'
import { Router } from '@angular/router';


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
  ) { }
  ngOnInit() {
  }
  add(email_id: string, name: string, last_name: string, password: string, gender: string, disability: string): void {
    this.hackatonService.postItem({ email_id, name, last_name, password, gender, disability } as Damaged)
      .subscribe(damaged => {
        this.damaged.push(damaged as unknown as Damaged);
      });
    this.goStartPage(email_id);
  }

  goStartPage(email_id: string): void {
    this.router.navigateByUrl('start/' + email_id);
  }
  /* getItem(): void {
    const aux = this.hackatonService.getItems()
      .subscribe(item => {
        this.damaged = (item as unknown as Damaged[]);
      });
    console.log(aux) */
  /*  this.hackatonService.postItem(this.damaged); */
  /* .subscribe(damaged => {
    this.damaged.push(damaged as unknown as Damaged);
  }); */
}
