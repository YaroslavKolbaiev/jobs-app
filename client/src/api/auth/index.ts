import {
  validateEmail,
  validatePassword,
} from "@/services/formValidationService";
import { accessTokenService } from "@/services/accessTokenService";
import type { GetUserResponse, UserCredentials } from "@/types";
import axios, { type AxiosProgressEvent } from "axios";
import { userJobsCache } from "@/cache";

const BASE_URL = import.meta.env.VITE_API_URL;

async function register(userCredentials: UserCredentials) {
  const errors = {
    email: validateEmail(userCredentials.email),
    password: validatePassword(userCredentials.password),
  };

  if (errors.email || errors.password) {
    throw new Error(errors.email || errors.password);
  }

  if (userCredentials.password !== userCredentials.confirmPassword) {
    throw new Error("password and confirm password do not match");
  }

  try {
    const response = await axios.post(
      `${BASE_URL}/api/auth/register`,
      userCredentials
    );

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.message);
    }
  }
}

async function login(email: string, password: string) {
  const errors = {
    email: validateEmail(email),
    password: validatePassword(password),
  };

  if (errors.email || errors.password) {
    throw new Error(errors.email || errors.password);
  }

  try {
    const response = await axios.post<GetUserResponse>(
      `${BASE_URL}/api/auth/token`,
      {
        email,
        password,
      },
      { withCredentials: true }
    );

    const { access_token } = response.data;

    if (access_token) {
      accessTokenService.save(access_token);
    }

    return response.data;
  } catch (error) {
    throw new Error("E-Mail or password is incorrect");
  }
}

async function getUser(): Promise<GetUserResponse> {
  try {
    const response = await axios.get<GetUserResponse>(`${BASE_URL}/api/me`, {
      withCredentials: true,
    });

    const { access_token } = response.data;

    if (access_token) {
      accessTokenService.save(access_token);
    }

    return response.data;
  } catch (error) {
    accessTokenService.remove();
    throw new Error("unauthorized");
  }
}

async function logout() {
  const accessToken = accessTokenService.get();

  if (!accessToken) {
    return;
  }

  await axios.post(`${BASE_URL}/api/auth/logout`, null, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
    withCredentials: true,
  });

  accessTokenService.remove();
  delete userJobsCache[accessToken];
}

async function uploadResume(
  formData: FormData,
  onUploadProgress: (progressEvent: AxiosProgressEvent) => void
) {
  const accessToken = accessTokenService.get();

  const response = await axios.post(`${BASE_URL}/api/upload/resume`, formData, {
    onUploadProgress,
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
    withCredentials: true,
  });

  return response.data;
}

export { login, getUser, register, logout, uploadResume };
