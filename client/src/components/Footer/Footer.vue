<script setup lang="ts">
import { reactive, ref } from "vue";
import IconCloseModal from "@/components/icons/IconCloseModal.vue";

const formData = reactive({
  name: "",
  email: "",
  message: "",
});

const isModal = ref(false);

const onSubmit = () => {
  console.log("Submited");

  Object.keys(formData).forEach((key) => {
    formData[key as keyof typeof formData] = "";
  });

  isModal.value = true;
};
</script>

<template>
  <div class="footer">
    <footer>
      <div>
        <h2>Send us a message</h2>
        <form @submit.prevent="onSubmit">
          <input v-model="formData.name" type="text" placeholder="Name" />
          <input v-model="formData.email" type="email" placeholder="Email" />
          <textarea v-model="formData.message" placeholder="Message"></textarea>
          <button class="button" type="submit">Send</button>
        </form>
      </div>

      <div>
        <h2>Contact us</h2>
        <p>call us</p>
        <strong class="phoneNumber">654 238 111</strong>
        <p>visit us</p>
        <strong>2905 Helm's Deep, Thrihyrne</strong>
      </div>

      <Transition name="fade">
        <div v-if="isModal" class="modal">
          <p>
            <button class="modal__button" @click="isModal = false">
              <IconCloseModal />
            </button>
            <br />
            Message was successfully sent!
          </p>
        </div>
      </Transition>
    </footer>
  </div>
</template>

<style scoped lang="scss">
@import "../../styles/transitions/fade.scss";
@import "../../styles/mixins.scss";
@import "../../styles/buttons.scss";

.footer {
  width: 100%;
  background-color: var(--headerFooter-bg);
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  position: relative;
}

footer {
  max-width: var(--max-width);
  margin: 0 auto;
  color: var(--header-text);
  padding: var(--py-mobile) var(--px-mobile);
  display: flex;
  flex-direction: column;
  gap: 40px;

  @include onTablet {
    flex-direction: row;
    justify-content: space-between;
    padding: 80px 80px 40px;
  }
}

h2 {
  font-size: 24px;
  margin-top: 0;

  @include onTablet {
    font-size: 36px;
  }
}

div {
  width: 100%;

  @include onTablet {
    width: 40%;
  }
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input,
textarea {
  border: none;
  border-bottom: 1px solid var(--header-text);
  padding: 20px 0;
  background-color: transparent;
  transition: border-bottom 300ms;
  color: var(--header-text);
  font-size: 12px;
  font-family: Poppins, sans-serif;

  &:focus {
    outline: none;
    border-bottom: 1px solid var(--c-blue);
  }

  @include onTablet {
    font-size: 16px;
  }
}

textarea {
  resize: none;
  height: 100px;
  margin-bottom: 60px;
}

p {
  margin-top: 40px;
  margin-bottom: 10px;
  text-transform: uppercase;
  font-size: 14px;

  @include onTablet {
    font-size: 20px;
  }
}

strong {
  font-size: 16px;

  @include onTablet {
    font-size: 24px;
  }
}

.modal {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;

  &__button {
    background: none;
    border: none;
    padding: 0;
    fill: #e0e0e0;
    transition: fill 300ms;
    cursor: pointer;

    &:hover {
      fill: #d71515;
    }
  }
}
</style>
