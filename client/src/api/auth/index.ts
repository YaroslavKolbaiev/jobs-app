import { validateEmail, validatePassword } from '@/utils';
import axios from 'axios';

const BASE_URL = import.meta.env.VITE_API_URL;

async function login(email: string, password: string) {
  const errors = {
    email: validateEmail(email),
    password: validatePassword(password),
  };

  if (errors.email || errors.password) {
    throw new Error(errors.email || errors.password);
  }

  try {
    const response = await axios.post(
      `${BASE_URL}/api/auth/token`,
      {
        email,
        password,
      },
      { withCredentials: true }
    );

    return response.data;
  } catch (error) {
    throw new Error('E-Mail or password is incorrect');
  }
}

export { login };
