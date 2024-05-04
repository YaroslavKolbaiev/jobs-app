<script setup lang="ts">
import { logout } from "../../api/auth";
import { useAuthStore } from "../../stores/auth";
import { useRouter } from "vue-router";
import useFetchData from "../../hooks/useFetchData";
import { watch } from "vue";

const emit = defineEmits(["errorEmited"]);

const useAuth = useAuthStore();
const router = useRouter();

const onLogout = async () => {
  logout();
  useAuth.logout();
  router.push("/");
};

const { isLoading, error, doRequest } = useFetchData(onLogout);

watch(error, () => {
  emit("errorEmited", error);
});
</script>

<template>
  <form @submit.prevent="doRequest">
    <button :disabled="isLoading" type="submit" class="button button--logout">
      Log out
    </button>
  </form>
</template>

<style scoped lang="scss">
@import "../../styles/buttons.scss";
</style>
