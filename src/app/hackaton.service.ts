import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {MessageService} from './message.service';
import {catchError, map, tap} from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {Damaged} from './damaged'

const httpOptions = {headers: new HttpHeaders({'Content-Type': 'application/json'})};



@Injectable({
  providedIn: 'root'
})
export class HackatonService {
  private hackatonURL = 'http://172.20.80.27:8080/User/'

  constructor(
    private http: HttpClient,
    private messageService: MessageService,

  ) { }
  
  getItems(): Observable<Damaged[]>{
    console.log("entro")
    return this.http.get<Damaged[]>(this.hackatonURL)
    .pipe(tap(_ => this.log('fetched DamagedFields')),
        catchError(this.handleError<Damaged[]>('getDamaged', []))
      );
  }

  getItem(id: number): Observable<Damaged>{
    const url= `${this.hackatonURL}${id}`;
    return this.http.get<Damaged>(url);
  }

  postItem(item: Damaged): Observable<Damaged>{
    console.log(typeof (item))
    return this.http.post<Damaged>(this.hackatonURL, item, httpOptions).pipe(
      tap((newItem: Damaged) => this.log(`added damaged w/ id=${newItem.email_id}`)),
      catchError(this.handleError<Damaged>('addDamaged'))
    );
  }

  updateItem(item: Damaged): Observable<any>{
    const id = typeof item === 'number' ? item : item.email_id;
    const url = `${this.hackatonURL}${id}`;
    return this.http.put(url, item, httpOptions);
  }

  deleteItem(item: Damaged | number): Observable<Damaged> {
    const id = typeof item === 'number' ? item : item.user_id;
    const url = `${this.hackatonURL}${id}`;

    return this.http.delete<Damaged>(url, httpOptions);
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.log(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }


}
