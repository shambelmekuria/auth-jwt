import axios from "axios";

const API_URL= "http://127.0.0.1:8000/api/users/"

export const registerUser = async (email:string,username:string,password:string)=>{
     try {
        const response = await axios.post("http://127.0.0.1:8000/api/users/register/", {email, username, password},
            {withCredentials: true}
        )
        return response.data;
    }
    catch (e) {
        throw new Error("Registration failed!");
    }

}

export const loginUser = async (email:string,password:string) => {

}
