return {
  "nvim-telescope/telescope-file-browser.nvim",
  dependencies = { "nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim" },
  vim.api.nvim_set_keymap(
    "n",
    "<leader>fb",
    ":Telescope file_browser <cr>",
    { noremap = false }
  ),
  -- open file_browser with the path of the current buffer
  vim.keymap.set(
    "n",
    "<leader>fk",
    ":Telescope file_browser path=%:p:h select_buffer=true <cr>",
    { noremap = true }
  )
}
