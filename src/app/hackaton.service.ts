import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {catchError, map, tap} from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {Damaged} from './damaged'

const httpOptions = {headers: new HttpHeaders({'Content-Type': 'application/json'})};



@Injectable({
  providedIn: 'root'
})
export class HackatonService {
  private hackatonURL = '172.20.80.27:8080/User/'

  constructor(
    private http: HttpClient,
  ) { }
  
  getItems(): Observable<Damaged[]>{
    return this.http.get<Damaged[]>(this.hackatonURL);
  }

  getItem(id: number): Observable<Damaged>{
    const url= `${this.hackatonURL}${id}`;
    return this.http.get<Damaged>(url);
  }

  postItem(item: Damaged): Observable<Damaged>{
    console.log(item)
    return this.http.post<Damaged>(this.hackatonURL, item, httpOptions);
  }

  updateItem(item: Damaged): Observable<any>{
    const id = typeof item === 'number' ? item : item.user_id;
    const url = `${this.hackatonURL}${id}`;
    return this.http.put(url, item, httpOptions);
  }

  deleteItem(item: Damaged | number): Observable<Damaged> {
    const id = typeof item === 'number' ? item : item.user_id;
    const url = `${this.hackatonURL}${id}`;

    return this.http.delete<Damaged>(url, httpOptions);
  }


}
