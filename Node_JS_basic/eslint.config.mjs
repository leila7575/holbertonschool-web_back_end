import globals from "globals";
import pluginJs from "@eslint/js";


export default [
  {
    files: ["**/*.js"], 
    languageOptions: {
      sourceType: "commonjs",
      ecmaVersion: 2021,
      globals:{
        ...globals.node,
      },
    },
  },

  {
    files: ["**/*.js"],
    languageOptions: { 
      globals:{
        ...globals.browser,
      },
    },
  },
    pluginJs.configs.recommended,
];