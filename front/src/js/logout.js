
import { push } from 'svelte-spa-router';

export const logout = () => {
    const storedUsername = localStorage.getItem('username');
    const storedPassword = localStorage.getItem('password');
    
    if(!!storedPassword){
        localStorage.removeItem('password');
    }
    if(!!storedUsername){
        localStorage.removeItem('username');
    }

    push('/');
}