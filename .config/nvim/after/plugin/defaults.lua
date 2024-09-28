vim.opt.relativenumber = true

require('telescope').load_extension 'file_browser'
require('telescope').load_extension 'fzf'
vim.keymap.set({"n"},"<leader>F",":Format<cr>",{desc='Format current buffer'})
