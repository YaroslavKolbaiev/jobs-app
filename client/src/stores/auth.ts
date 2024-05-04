import type { User } from '@/types';
import { defineStore } from 'pinia';

export const useAuthStore = defineStore({
  id: 'auth',
  state: (): { user: User | null } => ({
    user: null,
  }),
  actions: {
    login(data: User) {
      this.user = data;
    },
    logout() {
      this.user = null;
    },
  },
});
