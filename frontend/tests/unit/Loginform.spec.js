// tests/unit/LoginForm.spec.js
import { shallowMount } from '@vue/test-utils';
import LoginForm from '@/components/LoginForm.vue';

    describe('LoginForm.vue', () => {
    it('renders without errors', () => {
        const wrapper = shallowMount(LoginForm);
        expect(wrapper.exists()).toBe(true);
    });
    });